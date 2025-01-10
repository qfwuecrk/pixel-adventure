import unittest
from unittest.mock import patch, MagicMock
import pygame

from src.render import Render


class TestRender(unittest.TestCase):

    @patch("pygame.time.Clock")
    @patch("pygame.display.set_mode")
    def setUp(self, mock_set_mode, mock_clock):
        # 初始化 Render 实例
        self.render = Render()
        self.render.clock = mock_clock
        self.render.screen = mock_set_mode.return_value

    @patch("pygame.display.flip")
    @patch("pygame.event.get")
    def test_run_exits_on_quit_event(self, mock_event_get, mock_display_flip):
        # 模拟 QUIT 事件
        mock_event_get.return_value = [MagicMock(type=pygame.QUIT)]
        # 运行 Render 的 run 方法
        self.render.run()
        # 检查 running 是否被设置为 False
        self.assertFalse(self.render.running)

    @patch("pygame.display.flip")
    @patch("pygame.event.get")
    def test_run_continues_on_non_quit_event(
        self, mock_event_get, mock_display_flip
    ):
        # 模拟非 QUIT 事件
        mock_event_get.return_value = [MagicMock(type=pygame.KEYDOWN)]

        def stop_running(tick):
            self.render.running = False

        # 在第一次循环后停止运行
        self.render.clock.tick.side_effect = stop_running

        # 运行 Render 的 run 方法
        self.render.run()
        # 检查 running 是否被设置为 False
        self.assertFalse(self.render.running)


if __name__ == "__main__":
    unittest.main()
