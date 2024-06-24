"""
Defines typing for structures having specific meaning.
"""

from __future__ import annotations

from typing import Union

import pygame

Position = Union[pygame.Vector2, tuple[int, int]]
"""Alias for pygame.Vector2. A tuple[int, int] can alternatively be given in place of it."""
Margin = tuple[int, int, int, int]
"""Alias for tuple[int, int, int, int]"""
