def draw_snake_part(d_row, d_col, block, head, pic_1, pic_2, pic_3, pic_4):
    pic_1_rect = pic_1.get_rect()
    pic_2_rect = pic_2.get_rect()
    pic_3_rect = pic_3.get_rect()
    pic_4_rect = pic_4.get_rect()
    if d_row == 0 and d_col == 1 and block != head:
        pic_1_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                   SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == 0 and d_col == -1 and block != head:
        pic_2_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                  SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == 1 and d_col == 0 and block != head:
        pic_3_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                    SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    if d_row == -1 and d_col == 0 and block != head:
        pic_4_rect.topleft = (SIZE_BLOCK + block.y * SIZE_BLOCK + MARGIN * (block.y + 1),
                                 SIZE_BLOCK + block.x * SIZE_BLOCK + MARGIN * (block.x + 1))
    screen.blit(pic_1, pic_1_rect)
    screen.blit(pic_2, pic_2_rect)
    screen.blit(pic_3, pic_3_rect)
    screen.blit(pic_4, pic_4_rect)

def draw_head(d_row, d_col, new_head, pic_1, pic_2, pic_3, pic_4):
    pic_1_rect = pic_1.get_rect()
    pic_2_rect = pic_2.get_rect()
    pic_3_rect = pic_3.get_rect()
    pic_4_rect = pic_4.get_rect()
    if d_row == 0 and d_col == 1:
        pic_1_rect.topleft = (new_head.y * SIZE_BLOCK + MARGIN * new_head.y,
                              SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 1))
    if d_row == 0 and d_col == -1:
        pic_2_rect.topleft = (2 * SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 2),
                             SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 1))
    if d_row == 1 and d_col == 0:
        pic_3_rect.topleft = (SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 1),
                               new_head.x * SIZE_BLOCK + MARGIN * new_head.x)
    if d_row == -1 and d_col == 0:
        pic_4_rect.topleft = (SIZE_BLOCK + new_head.y * SIZE_BLOCK + MARGIN * (new_head.y + 1),
                            2 * SIZE_BLOCK + new_head.x * SIZE_BLOCK + MARGIN * (new_head.x + 2))
    pic_1.set_colorkey(ANOTHER_BLACK)
    pic_2.set_colorkey(ANOTHER_BLACK)
    pic_3.set_colorkey(ANOTHER_BLACK)
    pic_4.set_colorkey(ANOTHER_BLACK)
    screen.blit(pic_1, pic_1_rect)
    screen.blit(pic_2, pic_2_rect)
    screen.blit(pic_3, pic_3_rect)
    screen.blit(pic_4, pic_4_rect)
