//gcc -Wall -Wextra -g -o main main.c -D_POSIX_C_SOURCE=200809L -lraylib
#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <raylib.h>

#define MAX_OUTPUT 8192

void draw_multiline_text(Font font, const char *text, int x, int y, int maxWidth, int fontSize) {
    int len = strlen(text);
    int start = 0;

    while (start < len) {
        int end = start + 1;

        while (end <= len) {
            char temp[1024];
            strncpy(temp, text + start, end - start);
            temp[end - start] = '\0';

            float w = MeasureTextEx(font, temp, fontSize, 2).x;

            if (w > maxWidth) {
                end--;
                break;
            }
            end++;
        }

        if (end == start) end++; // 防止死循环

        char line[1024];
        strncpy(line, text + start, end - start);
        line[end - start] = '\0';

        DrawTextEx(font, line, (Vector2){x, y}, fontSize, 2, WHITE);

        y += fontSize + 5;
        start = end;
    }
}

char* run_ocr(const char* image) {
    static char result[MAX_OUTPUT];
    result[0] = '\0';

    char cmd[256];
    snprintf(cmd, sizeof(cmd),
             "tesseract %s stdout -l jpn 2>/dev/null",
             image);

    FILE *fp = popen(cmd, "r");
    if (!fp) return NULL;

    char buffer[256];

    while (fgets(buffer, sizeof(buffer), fp)) {
        strncat(result, buffer,
                MAX_OUTPUT - strlen(result) - 1);
    }

    pclose(fp);

    return result;
}

int main() {

    InitWindow(900, 300, "GalTranslater");
    SetTargetFPS(30);

    char last_text[MAX_OUTPUT] = {0};
    char current_text[MAX_OUTPUT] = {0};


    int codepoints[20992];
    int count = 0;

    // 平假名
    for (int i = 0x3040; i <= 0x309F; i++) {
        codepoints[count++] = i;
    }

    // 片假名
    for (int i = 0x30A0; i <= 0x30FF; i++) {
        codepoints[count++] = i;
    }

    // 常用汉字
    for (int i = 0x4E00; i <= 0x9FFF; i++) {
        codepoints[count++] = i;
    }

    Font font = LoadFontEx("QiushuiShotai.ttf", 50, codepoints, count);
    // ⚠️ 你需要准备一个支持日文的字体

    printf("font id: %d\n", font.texture.id);


    while (!WindowShouldClose())
    {
        // 🔁 每隔一段时间 OCR 一次
        static float timer = 0;
        timer += GetFrameTime();

        if (timer > 0.5f) { // 每0.5秒识别一次
            timer = 0;

            char *text = run_ocr("text.png");

            if (text && strlen(text) > 0) {
                // 去重
                if (strcmp(text, last_text) != 0) {
                    strncpy(current_text, text, MAX_OUTPUT - 1);
                    strncpy(last_text, text, MAX_OUTPUT - 1);

                    printf("新文本:\n%s\n", current_text);
                }
            }
        }

        BeginDrawing();
            ClearBackground(BLACK);
            int screenWidth = GetScreenWidth();
            int screenHeight = GetScreenHeight();

            // 半透明黑框
            //DrawRectangle(0, screenHeight - 200, screenWidth, 200, (Color){0, 100,0, 180});

            // 画文字
            draw_multiline_text(font, current_text, 100, screenHeight - 200, screenWidth - 40, 50);

        EndDrawing();
    }

    UnloadFont(font);
    CloseWindow();

    return 0;
}