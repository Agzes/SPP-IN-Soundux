# Author: Giuseppe
from __future__ import annotations

from typing import Optional, Sequence

import dearpygui.dearpygui as dpg

name = """main"""
styles: dict[int, Sequence[float]] = {
    dpg.mvStyleVar_Alpha: [1.0],
    dpg.mvStyleVar_WindowPadding: [8.0, 8.0],
    dpg.mvStyleVar_WindowRounding: [0.0],
    dpg.mvStyleVar_WindowBorderSize: [0.0],
    dpg.mvStyleVar_WindowMinSize: [30.0, 30.0],
    dpg.mvStyleVar_WindowTitleAlign: [0.5, 0.5],
    dpg.mvStyleVar_ChildRounding: [3.0],
    dpg.mvStyleVar_ChildBorderSize: [0.0],
    dpg.mvStyleVar_PopupRounding: [3.0],
    dpg.mvStyleVar_PopupBorderSize: [0.0],
    dpg.mvStyleVar_FramePadding: [5.0, 3.5],
    dpg.mvStyleVar_FrameRounding: [4.0],
    dpg.mvStyleVar_FrameBorderSize: [0.0],
    dpg.mvStyleVar_ItemSpacing: [5.0, 4.0],
    dpg.mvStyleVar_ItemInnerSpacing: [5.0, 5.0],
    dpg.mvStyleVar_CellPadding: [4.0, 2.0],
    dpg.mvStyleVar_IndentSpacing: [5.0],
    dpg.mvStyleVar_ScrollbarSize: [15.0],
    dpg.mvStyleVar_ScrollbarRounding: [3.0],
    dpg.mvStyleVar_GrabMinSize: [15.0],
    dpg.mvStyleVar_GrabRounding: [3.0],
    dpg.mvStyleVar_TabRounding: [3.0],
    dpg.mvStyleVar_ButtonTextAlign: [0.5, 0.5],
    dpg.mvStyleVar_SelectableTextAlign: [0.0, 0.0],
}
colors: dict[int, Sequence[int, int, int, Optional[int]]] = {
    dpg.mvThemeCol_Text: [255, 255, 255, 255],
    dpg.mvThemeCol_TextDisabled: [70, 81, 115, 140],
    dpg.mvThemeCol_WindowBg: [20, 22, 26, 255],
    dpg.mvThemeCol_ChildBg:  [24, 26, 30, 100],
    dpg.mvThemeCol_PopupBg:  [20, 22, 26, 255],
    dpg.mvThemeCol_Border:  [40, 43, 49, 255],
    dpg.mvThemeCol_BorderShadow: [20, 22, 26, 140],
    dpg.mvThemeCol_FrameBg:   [29, 32, 39, 255],
    dpg.mvThemeCol_FrameBgHovered: [40, 43, 49, 100],
    dpg.mvThemeCol_FrameBgActive:  [40, 43, 49, 140],
    dpg.mvThemeCol_TitleBg:  [12, 14, 18, 140],
    dpg.mvThemeCol_TitleBgActive:  [12, 14, 18, 140],
    dpg.mvThemeCol_TitleBgCollapsed:  [20, 22, 26, 140],
    dpg.mvThemeCol_MenuBarBg:  [25, 27, 31, 140],
    dpg.mvThemeCol_ScrollbarBg:  [12, 14, 18, 140],
    dpg.mvThemeCol_ScrollbarGrab:  [30, 34, 38, 140],
    dpg.mvThemeCol_ScrollbarGrabHovered:  [40, 43, 49, 140],
    dpg.mvThemeCol_ScrollbarGrabActive:  [30, 34, 38, 140],
    dpg.mvThemeCol_CheckMark:  [248, 255, 127, 140],
    dpg.mvThemeCol_SliderGrab:  [248, 255, 127, 140],
    dpg.mvThemeCol_SliderGrabActive:  [255, 203, 127, 140],
    dpg.mvThemeCol_Button: [50, 50, 50, 170],
    dpg.mvThemeCol_ButtonHovered: [47, 48, 50, 170],
    dpg.mvThemeCol_ButtonActive:  [39, 39, 39, 170],
    dpg.mvThemeCol_Header:  [36, 41, 53, 140],
    dpg.mvThemeCol_HeaderHovered: [27, 27, 27, 140],
    dpg.mvThemeCol_HeaderActive:  [20, 22, 26, 140],
    dpg.mvThemeCol_Separator:  [33, 38, 49, 140],
    dpg.mvThemeCol_SeparatorHovered:  [40, 47, 64, 140],
    dpg.mvThemeCol_SeparatorActive:  [40, 47, 64, 140],
    dpg.mvThemeCol_ResizeGrip:  [37, 37, 37, 140],
    dpg.mvThemeCol_ResizeGripHovered: [248, 255, 127, 140],
    dpg.mvThemeCol_ResizeGripActive:  [255, 255, 255, 140],
    dpg.mvThemeCol_Tab:  [0, 22, 26, 140],
    dpg.mvThemeCol_TabHovered:  [30, 34, 38, 140],
    dpg.mvThemeCol_TabActive:  [30, 34, 38, 140],
    dpg.mvThemeCol_TabUnfocused:  [20, 22, 26, 140],
    dpg.mvThemeCol_TabUnfocusedActive: [32, 70, 145, 140],
    dpg.mvThemeCol_PlotLines:  [133, 153, 179, 140],
    dpg.mvThemeCol_PlotLinesHovered:  [10, 250, 250, 140],
    dpg.mvThemeCol_PlotHistogram: [66,66,66, 140],
    dpg.mvThemeCol_PlotHistogramHovered: [244, 244, 244, 140],
    dpg.mvThemeCol_TableHeaderBg:  [12, 14, 18, 140],
    dpg.mvThemeCol_TableBorderStrong: [12, 14, 18, 140],
    dpg.mvThemeCol_TableBorderLight:  [0, 0, 0, 140],
    dpg.mvThemeCol_TableRowBg:  [30, 34, 38, 140],
    dpg.mvThemeCol_TableRowBgAlt:  [25, 27, 31, 140],
    dpg.mvThemeCol_TextSelectedBg: [239, 239, 239, 140],
    dpg.mvThemeCol_DragDropTarget: [127, 131, 255, 140],
    dpg.mvThemeCol_NavHighlight:  [68, 74, 255, 140],
    dpg.mvThemeCol_NavWindowingHighlight: [127, 131, 255, 140],
    dpg.mvThemeCol_NavWindowingDimBg:  [50, 45, 139, 128],
    dpg.mvThemeCol_ModalWindowDimBg:  [50, 45, 139, 128],

}
