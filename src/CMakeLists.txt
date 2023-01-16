
add_executable(pico_drum_machine
    main.c
    )

#add_library(samples
#    samples.c samples.h
#    )

target_link_libraries(pico_drum_machine PRIVATE 
    pico_stdlib 
    pico_audio_i2s
#    ${CMAKE_SOURCE_DIR}/src/samples.a
    )

pico_add_extra_outputs(pico_drum_machine)
