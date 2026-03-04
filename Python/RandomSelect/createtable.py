import pandas as pd
from sqlalchemy import create_engine, text, inspect
import os
import sys

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'database': 'class42'
}

# 文件夹路径配置
FOLDER_PATH = 'Details/42list'

# 固定的表头
FIXED_COLUMNS = ['Date', 'Score', 'Time']


def create_db_engine():
    """创建数据库连接引擎"""
    try:
        connection_string = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset=utf8mb4"
        engine = create_engine(connection_string)

        # 测试连接
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine
    except Exception as e:
        print(f"❌ 数据库连接失败: {e}")
        return None


def extract_table_name(file_path):
    """从文件名提取表名"""
    file_name = os.path.basename(file_path)
    table_name = os.path.splitext(file_name)[0]

    # 清理表名
    table_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in table_name)

    # 如果以数字开头，添加前缀
    if table_name and table_name[0].isdigit():
        table_name = 'tbl_' + table_name

    # 如果表名为空，使用默认名
    if not table_name:
        table_name = 'table_' + str(hash(file_name) % 1000)

    # 确保表名长度不超过64个字符
    return table_name[:60]


def read_data_file(file_path):
    """读取数据文件"""
    file_ext = os.path.splitext(file_path)[1].lower()

    try:
        # 根据文件类型读取数据
        if file_ext == '.csv':
            # 读取CSV文件，不跳过空行
            df = pd.read_csv(file_path, encoding='utf-8', skip_blank_lines=False,header=None)
        elif file_ext in ['.xlsx', '.xls']:
            # 读取Excel文件，不跳过空行
            df = pd.read_excel(file_path, keep_default_na=False)
        elif file_ext == '.json':
            df = pd.read_json(file_path)
        elif file_ext == '.txt':
            # 尝试不同的分隔符
            try:
                df = pd.read_csv(file_path, sep='\t', encoding='utf-8', skip_blank_lines=False)
            except:
                try:
                    df = pd.read_csv(file_path, sep=',', encoding='utf-8', skip_blank_lines=False)
                except:
                    try:
                        df = pd.read_csv(file_path, sep=';', encoding='utf-8', skip_blank_lines=False)
                    except:
                        df = pd.read_csv(file_path, sep=None, engine='python', encoding='utf-8', skip_blank_lines=False)
        else:
            print(f"❌ 不支持的文件格式: {file_ext}")
            return None

        return df

    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return None


def process_dataframe(df):
    """处理数据框，确保只有Date, Score, Time三列，保留所有数据"""
    try:
        # 检查数据框是否为空
        if df is None:
            print("  警告: 数据框为None")
            return pd.DataFrame(columns=FIXED_COLUMNS)

        # 重置索引，确保所有行都被处理
        df = df.reset_index(drop=True)

        # 显示原始数据信息
        print(f"  原始数据: {len(df)} 行，{len(df.columns)} 列")

        # 如果数据框为空，返回空数据框
        if df.empty:
            print("  警告: 数据框为空")
            return pd.DataFrame(columns=FIXED_COLUMNS)

        # 创建结果数据框
        result = pd.DataFrame(index=df.index)

        # 处理每列数据
        for i, fixed_col in enumerate(FIXED_COLUMNS):
            if i < len(df.columns):
                # 获取第i列数据
                col_data = df.iloc[:, i].copy()

                # 如果列名包含特殊字符，清理列名
                if isinstance(col_data.name, str):
                    col_data.name = fixed_col

                # 添加到结果数据框
                result[fixed_col] = col_data
            else:
                # 如果文件列数不足，用空值填充
                result[fixed_col] = pd.NA

        print(f"  处理后数据: {len(result)} 行，{len(result.columns)} 列")

        # 确保列顺序正确
        result = result[FIXED_COLUMNS]

        # 显示数据信息
        print(f"  Date列非空值: {result['Date'].notna().sum()}")
        print(f"  Score列非空值: {result['Score'].notna().sum()}")
        print(f"  Time列非空值: {result['Time'].notna().sum()}")

        return result

    except Exception as e:
        print(f"  处理数据框时出错: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame(columns=FIXED_COLUMNS)


def create_table(engine, table_name):
    """创建具有固定列的表（不包含时间戳）"""
    try:
        with engine.connect() as conn:
            # 检查表是否存在
            inspector = inspect(engine)
            if table_name in inspector.get_table_names():
                print(f"  表 '{table_name}' 已存在，删除重建")
                conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))
                conn.commit()

            # 创建具有固定列的表，不包含imported_at时间戳
            create_sql = f"""
            CREATE TABLE `{table_name}` (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `Date` VARCHAR(255),
                `Score` DECIMAL(10, 2),
                `Time` VARCHAR(100)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """

            conn.execute(text(create_sql))
            conn.commit()

            print(f"  表 '{table_name}' 创建成功 (列: id, Date, Score, Time)")
            return True

    except Exception as e:
        print(f"❌ 创建表失败: {e}")
        return False


def insert_data(engine, table_name, df):
    """插入数据到表"""
    try:
        # 确保列名正确
        if list(df.columns) != FIXED_COLUMNS:
            print(f"  警告: 列名不匹配，重新命名列")
            df = df.copy()
            # 确保只有三列，并按正确顺序命名
            if len(df.columns) > 3:
                df = df.iloc[:, :3]
            df.columns = FIXED_COLUMNS[:len(df.columns)]

        # 确保数据框不为空
        if df.empty:
            print("  警告: 数据框为空，跳过插入")
            return False

        # 处理NaN/NA值为None（NULL）
        df = df.where(pd.notnull(df), None)

        # 尝试转换Score列为数值类型，但保留原始值如果转换失败
        if 'Score' in df.columns:
            try:
                # 尝试转换为数值，转换失败的设为None
                df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
            except Exception as e:
                print(f"  转换Score列时出错: {e}")
                # 如果转换失败，保持原样，让数据库处理
                pass

        # 显示要插入的数据信息
        print(f"  准备插入 {len(df)} 行数据")

        # 使用to_sql插入数据
        # 使用if_exists='append'确保不会覆盖已有数据（表已清空）
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',  # 由于我们之前删除了表，这里用append
            index=False,
            chunksize=1000,
            method='multi'
        )

        # 获取插入的行数
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`"))
            row_count = result.scalar()

        print(f"  成功插入 {row_count} 行数据")

        # 验证数据是否全部插入
        if row_count != len(df):
            print(f"  警告: 插入行数({row_count})与数据框行数({len(df)})不匹配")

        return True

    except Exception as e:
        print(f"❌ 插入数据失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def import_single_file(engine, file_path):
    """导入单个文件"""
    print(f"\n📤 开始导入文件: {os.path.basename(file_path)}")

    # 提取表名
    table_name = extract_table_name(file_path)
    print(f"  表名: {table_name}")

    # 读取原始数据
    raw_df = read_data_file(file_path)
    if raw_df is None:
        print(f"❌ 读取文件失败")
        return False

    # 处理数据
    df = process_dataframe(raw_df)

    # 检查处理后的数据
    if df.empty:
        print(f"❌ 处理后的数据为空")
        # 显示原始数据前几行
        if raw_df is not None and not raw_df.empty:
            print("  原始数据前5行:")
            print(raw_df.head().to_string())
        return False

    # 显示前几行预览
    print("  数据预览 (前5行):")
    print(df.head().to_string())

    # 显示最后几行预览
    print("  数据预览 (后5行):")
    print(df.tail().to_string())

    # 创建表
    if not create_table(engine, table_name):
        return False

    # 插入数据
    if not insert_data(engine, table_name, df):
        return False

    print(f"✅ 文件导入完成: {os.path.basename(file_path)} -> {table_name}")
    return True


def main():
    print("=" * 60)
    print("🚀 开始批量导入文件到MySQL")
    print("=" * 60)
    print(f"固定表头: {', '.join(FIXED_COLUMNS)}")
    print(f"文件夹路径: {FOLDER_PATH}")
    print(f"数据库: {DB_CONFIG['database']}")
    print("=" * 60)

    # 连接到数据库
    engine = create_db_engine()
    if not engine:
        return

    # 检查文件夹
    if not os.path.exists(FOLDER_PATH):
        print(f"❌ 文件夹不存在: {FOLDER_PATH}")
        # 尝试创建文件夹
        try:
            os.makedirs(FOLDER_PATH, exist_ok=True)
            print(f"✅ 已创建文件夹: {FOLDER_PATH}")
        except Exception as e:
            print(f"❌ 创建文件夹失败: {e}")
        return

    # 获取所有支持的文件
    supported_extensions = ['.csv', '.xlsx', '.xls', '.json', '.txt']
    files = []

    for item in os.listdir(FOLDER_PATH):
        item_path = os.path.join(FOLDER_PATH, item)
        if os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1].lower()
            if file_ext in supported_extensions:
                files.append(item_path)

    if not files:
        print("❌ 未找到可导入的文件")
        print("支持的文件格式: .csv, .xlsx, .xls, .json, .txt")
        print(f"文件夹内容: {os.listdir(FOLDER_PATH)}")
        return

    print(f"📁 找到 {len(files)} 个支持的文件:")
    for i, file_path in enumerate(files, 1):
        print(f"  {i}. {os.path.basename(file_path)}")

    # 开始导入
    print("\n" + "=" * 60)
    print("开始导入文件...")
    print("=" * 60)

    success_count = 0
    failed_files = []

    for i, file_path in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] ", end="")

        try:
            success = import_single_file(engine, file_path)
            if success:
                success_count += 1
            else:
                failed_files.append({
                    'file': os.path.basename(file_path),
                    'reason': '导入失败'
                })
        except Exception as e:
            print(f"❌ 导入过程中出错: {e}")
            import traceback
            traceback.print_exc()
            failed_files.append({
                'file': os.path.basename(file_path),
                'reason': f'异常: {e}'
            })

    # 显示统计结果
    print("\n" + "=" * 60)
    print("📊 导入统计结果")
    print("=" * 60)
    print(f"总文件数: {len(files)}")
    print(f"成功导入: {success_count}")
    print(f"失败: {len(files) - success_count}")

    if failed_files:
        print("\n❌ 失败的文件:")
        for item in failed_files:
            print(f"  - {item['file']}: {item['reason']}")

    if success_count > 0:
        print("\n✅ 导入完成！")

        # 列出所有表并显示每个表的数据量
        print("\n" + "=" * 60)
        print("📋 数据库中的表:")
        print("=" * 60)

        try:
            inspector = inspect(engine)
            tables = inspector.get_table_names()

            if tables:
                total_rows = 0
                for table_name in tables:
                    columns = inspector.get_columns(table_name)
                    with engine.connect() as conn:
                        result = conn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`"))
                        row_count = result.scalar()
                        total_rows += row_count

                    print(f"表: {table_name}")
                    print(f"  行数: {row_count}")
                    # 显示列信息
                    col_names = [col['name'] for col in columns if col['name'] != 'id']
                    print(f"  列: {', '.join(col_names)}")

                    # 显示前2行数据示例
                    if row_count > 0:
                        data_result = conn.execute(text(f"SELECT * FROM `{table_name}` LIMIT 2"))
                        print("  示例数据:")
                        for row in data_result:
                            # 只显示非id列
                            row_data = dict(row._mapping)
                            row_data.pop('id', None)
                            print(f"    {row_data}")
                    print("-" * 40)

                print(f"\n📈 总计: {len(tables)} 张表，{total_rows} 行数据")
            else:
                print("数据库中没有表")

        except Exception as e:
            print(f"获取表信息失败: {e}")
    else:
        print("\n❌ 导入失败，请检查错误信息")


if __name__ == "__main__":
    main()