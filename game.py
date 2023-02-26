#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

// 定义游戏区域的大小
const int width = 20;
const int height = 20;

// 定义蛇和食物的结构体
struct Snake
{
    int x, y;
};

struct Food
{
    int x, y;
};

// 定义全局变量
Snake snake[100];
Food food;
int nSnake, score;

// 初始化游戏
void Initialize()
{
    // 初始化蛇的位置
    snake[0].x = width / 2;
    snake[0].y = height / 2;
    nSnake = 1;

    // 随机生成食物的位置
    srand(time(NULL));
    food.x = rand() % width;
    food.y = rand() % height;

    score = 0;
}

// 显示游戏界面
void Draw()
{
    system("cls"); // 清屏

    // 输出游戏区域
    for (int i = 0; i <= height; i++)
    {
        for (int j = 0; j <= width; j++)
        {
            if (i == 0 || i == height || j == 0 || j == width)
                cout << "#";
            else if (i == food.y && j == food.x)
                cout << "F";
            else
            {
                bool isPrint = false;
                for (int k = 0; k < nSnake; k++)
                {
                    if (snake[k].x == j && snake[k].y == i)
                    {
                        cout << "O";
                        isPrint = true;
                    }
                }
                if (!isPrint)
                    cout << " ";
            }
        }
        cout << endl;
    }

    // 输出得分
    cout << "Score: " << score << endl;
}

// 处理键盘输入
void Input()
{
    if (_kbhit())
    {
        switch (_getch())
        {
        case 'w':
            for (int i = nSnake - 1; i > 0; i--)
                snake[i] = snake[i - 1];
            snake[0].y--;
            break;
        case 's':
            for (int i = nSnake - 1; i > 0; i--)
                snake[i] = snake[i - 1];
            snake[0].y++;
            break;
        case 'a':
            for (int i = nSnake - 1; i > 0; i--)
                snake[i] = snake[i - 1];
            snake[0].x--;
            break;
        case 'd':
            for (int i = nSnake - 1; i > 0; i--)
                snake[i] = snake[i - 1];
            snake[0].x++;
            break;
        }
    }
}

// 判断游戏是否结束
bool IsGameOver()
{
    // 判断是否撞墙
    if (snake[0].x == 0 || snake[0].x == width || snake[0].y == 0 || snake[0].y == height)
        return true;

    // 判断是否撞到自己的身体
    for (int i = 1; i < nSnake
