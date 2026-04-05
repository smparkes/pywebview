from __future__ import annotations

from collections.abc import Callable
from typing import Any


class Menu:
    def __init__(self, title: str, items: list[Menu | MenuAction | MenuSeparator] = []) -> None:
        """
        Args:
            title: the menu or submenu title
            items: the contents of the menu (can consist of Menu, MenuAction, or MenuSeparator instances)
        """
        self.title = title
        self.items = items


class MenuAction:
    def __init__(
        self,
        title: str,
        function: Callable[[], Any] | None = None,
        key_equivalent: str = '',
        key_modifiers: int = 0,
        enabled_flag: str = '',
        checked_flag: str = '',
        standard_selector: str = '',
        sf_symbol: str = '',
    ) -> None:
        self.title = title
        self.function = function
        # macOS key equivalent (e.g. ',' for Cmd+,). Empty string = no shortcut.
        # On non-macOS platforms this is currently ignored.
        self.key_equivalent = key_equivalent
        # NSEventModifierFlags bitmask. If 0 while key_equivalent is set, AppKit
        # defaults to Command. Pass an explicit mask (e.g. Cmd | Shift) for
        # multi-modifier shortcuts.
        self.key_modifiers = key_modifiers
        # Optional flag name. If set, the menu item's enabled state is driven
        # by the flag value set via set_menu_flag(). Default missing flag =
        # enabled=False (item greyed until the flag is set to True).
        # Empty string = always enabled.
        self.enabled_flag = enabled_flag
        # Optional flag name. If set, the menu item's checked state (checkmark)
        # is driven by the flag value set via set_menu_check(). Default missing
        # flag = unchecked. Empty string = never checked.
        self.checked_flag = checked_flag
        # Optional AppKit selector (e.g. 'cut:', 'paste:'). If set, the menu
        # item uses this selector with target=nil so Cocoa routes it to the
        # first responder (giving correct automatic enable/disable via the
        # responder's -respondsToSelector:/-validateUserInterfaceItem:).
        self.standard_selector = standard_selector
        # Optional SF Symbol name (e.g. 'plus', 'doc.on.doc'). macOS 11+ only.
        # Ignored on older systems or other platforms.
        self.sf_symbol = sf_symbol


class MenuSeparator:
    pass
