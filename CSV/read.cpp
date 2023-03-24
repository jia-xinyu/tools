#include <iostream>
#include <istream>
#include <streambuf>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdlib.h>

int main()
{
    std::ifstream csv_data("test.csv", std::ios::in);
    std::string line;

    if (!csv_data.is_open())
    {
        std::cout << "Error: opening file fail" << std::endl;
        std::exit(1);
    }

    std::istringstream sin;         //将整行字符串line读入到字符串istringstream中
    std::vector<std::string> words; //声明一个字符串向量
    std::string word;

    // 读取标题行
    std::getline(csv_data, line);
    // 读取数据
    while (std::getline(csv_data, line))
    {
        sin.clear();
        sin.str(line);
        words.clear();
        while (std::getline(sin, word, ',')) //将字符串流sin中的字符读到field字符串中，以逗号为分隔符
        {
            words.push_back(word); //将每一格中的数据逐个push
            std::cout << word;
            // std::cout << atol(word.c_str());
        }
        std::cout << std::endl;
        // do something。。。
    }
    csv_data.close();
    return 0;
}

