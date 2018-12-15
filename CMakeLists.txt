project(CleopheeBot NONE)

cmake_minimum_required(VERSION 2.8)

message("ENV{CHATSCRIPTINSTALLDIR} $ENV{CLEOPHEECHATSCRIPTINSTALLDIR}")
set(ChatScriptInstallDir $ENV{CLEOPHEECHATSCRIPTINSTALLDIR})

message("ENV{LIMA_PACKRUN} $ENV{LIMA_PACKRUN}")
set(LIMA_PACKRUN $ENV{LIMA_PACKRUN})

add_subdirectory(Resources)
add_subdirectory(cleopheeweb)

# install(DIRECTORY db DESTINATION ${CMAKE_INSTALL_PREFIX})

if (UNIX)
  set(CHATSCRIPT_BIN "./LinuxChatScript64")
else()
  set(CHATSCRIPT_BIN "chatscript.exe")
endif()

# configure_file(chatscript_settings.py chatscript_settings.py @ONLY)

install(FILES
#     ${CMAKE_CURRENT_BINARY_DIR}/chatscript_settings.py
    README.md
    run_cleophee.py
    chatscript.py
  DESTINATION ${CMAKE_INSTALL_PREFIX}
)
