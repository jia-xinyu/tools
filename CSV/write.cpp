#include <iostream>
#include <fstream>

int main()
{
    std::ofstream outFile;
    outFile.open("test.csv", std::ios::out | std::ios::trunc);
    // 写入标题行
    outFile << "name" << ','
            << "income" << ','
            << "expenditure" << ','
            << "addr" << std::endl;
    // ********写入两行数据*********
    // 写入字符串(数字)
    outFile << "zhangsan" << ','
            << "3000" << ','
            << "1200" << ','
            << "中国 北京市" << std::endl;
    // 写入浮点数(转为字符串)
    outFile << "lisi" << ','
            << std::to_string(2032.1) << ','
            << std::to_string(789.2) << ','
            << "中国 陕西省" << std::endl;
    outFile.close();
    return 0;
}

