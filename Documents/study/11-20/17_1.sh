input_file=$1
N=$2

# 行数を取得
total_lines=$(wc -l < "$input_file")

# 分割後の行数を計算
lines_per_file=$((total_lines / N))

# 分割実行
split -l "$lines_per_file" "$input_file" split_file_
