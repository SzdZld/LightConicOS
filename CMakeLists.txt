cmake_minimum_required(VERSION 3.10)
project(JMOT_lib VERSION 0.3.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

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