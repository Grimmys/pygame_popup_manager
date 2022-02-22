"""
Defines typing for structures having specific meaning.
"""

from __future__ import annotations

import pygame

Position = pygame.Vector2
"""Alias for pygame.Vector2. A tuple[int, int] can alternatively be given in place of it."""
Margin = tuple[int, int, int, int]
"""Alias for tuple[int, int, int, int]"""
