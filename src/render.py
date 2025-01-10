"""
render.py

这是一个使用 Pygame 库的简单渲染模块。Render 类初始化 Pygame 并设置窗口大小，
然后在主循环中处理事件、更新屏幕显示并控制帧率。当接收到退出事件时，主循环结束并退出 Pygame。
"""

import pygame


class Render:
    def __init__(self):
        pygame.init()  # 初始化 Pygame
        self.screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
        self.clock = pygame.time.Clock()  # 创建时钟对象
        self.running = True  # 控制主循环的标志位
        self.fps = 60  # 帧率

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 处理退出事件
                    self.running = False

            self.screen.fill("purple")  # 填充屏幕颜色
            pygame.display.flip()  # 更新显示
            self.clock.tick(self.fps)  # 控制帧率

        pygame.quit()  # 退出 Pygame
