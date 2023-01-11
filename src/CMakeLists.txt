add_executable(sine_wave_i2s
    sine_wave_i2s.c    
    )

target_link_libraries(sine_wave_i2s PRIVATE
    pico_stdlib
    pico_audio_i2s
    )

target_compile_definitions(sine_wave_i2s PRIVATE
    # SET UP MONO OUTPUT 
    PICO_AUDIO_I2S_MONO_INPUT=1
    # for defining in code can ommit and just include pico/pico_audio_i2s.h
    USE_AUDIO_I2S=1
    )
pico_add_extra_outputs(sine_wave_i2s)
