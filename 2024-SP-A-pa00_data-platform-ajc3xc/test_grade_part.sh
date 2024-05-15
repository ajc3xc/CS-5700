
declare -A file_arr
file_arr=(
    ["image_diff.png"]="PNG image data"
    ["image_py-debug1.png"]="PNG image data"
    ["image_py-debug2.png"]="PNG image data"
    ["pandas_explore.py"]="Python script"
)

filename = "pandas_explore.py"
echo file "pandas_explore.py"
exit 1

first="0"
for exist_file in "${!file_arr[@]}"; do
    if [ $first = "0" ]; then
        section
        echo "$ORANGE""Below here, we will run tests for existence of files and their type data:""$RESET"
        first="1"
        keepgoing
    fi
    subsection
    echo -e "Checking for the existence of '$exist_file' and its containing type of data:" "'${arr["$exist_file"]}.'"
    [ -f "$exist_file" ] && file "$exist_file" | grep "${arr["$exist_file"]}" >/dev/null 2>&1
    grade_update \""$exist_file\" with type containing \"${arr["$exist_file"]}\" existed" 100 0
done