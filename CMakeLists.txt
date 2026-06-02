cmake_minimum_required(VERSION 3.10)
project(JMOT_lib VERSION 0.3.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

# 设置构建阶段的输出目录（可选，根据你的需求决定是否添加）
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

# JMOT_utils library
add_library(JMOT_utils SHARED
    src/JMOT_utils.cpp
)
target_include_directories(JMOT_utils PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# JMOT_client library
add_library(JMOT_client SHARED
    src/JMOT_client.cpp
)
target_include_directories(JMOT_client PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
target_link_libraries(JMOT_client PUBLIC JMOT_utils)
if (WIN32)
    target_link_libraries(JMOT_client PUBLIC ws2_32)
endif ()

# JMOT core library
add_library(JMOT SHARED
    src/JMOT.cpp
        src/control.cpp
        src/craft.cpp
        src/part.cpp
        src/planet.cpp
        src/time.cpp
        src/misc.cpp
        src/extra.cpp
)
target_include_directories(JMOT PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
target_link_libraries(JMOT PUBLIC JMOT_client JMOT_utils)

include(GNUInstallDirs)

install(TARGETS JMOT_utils JMOT_client JMOT
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}   # Windows下 .dll 去 bin 目录
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}   # Linux下 .so 或 Windows下 .dll.a 去 lib 目录
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}   # Windows下 .lib 或 Linux下 .a 去 lib 目录
)

# 安装所有的头文件到 include 目录
install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})