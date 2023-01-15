add_executable(pico_drum_machine
    main.c
    )

target_link_libraries(sine_wave_i2s PRIVATE
    pico_stdlib
    pico_audio_i2s
    )

target_compile_definitions(sine_wave_i2s PRIVATE
    PICO_AUDIO_I2S_MONO_INPUT=1
    USE_AUDIO_I2S=1
    )

