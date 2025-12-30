(GAME_LOOP)
    @24576         // Read keyboard input
    D=M
    @UPDATE_INPUT
    0;JMP

(UPDATE_INPUT)
    // Input logic here

    @UPDATE_PADDLE
    0;JMP

(UPDATE_PADDLE)
    // Paddle movement logic here

    @DRAW_SCREEN
    0;JMP

(DRAW_SCREEN)
    // Drawing logic here

    @GAME_LOOP
    0;JMP