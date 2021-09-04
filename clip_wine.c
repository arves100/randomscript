// gcc -oclip.exe clip.c -lUser32
// cl clip.c User32.lib
// Should fail on Wine 6.10...

#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#define pac85 main

int pac85(int argc, char** argv)
{
	RECT rc;
	
	UNREFERENCED_PARAMETER(argc);
	UNREFERENCED_PARAMETER(argv);
	
	rc.top = 100;
	rc.left = 100;
	rc.right = 400;
	rc.bottom = 400;
	
	ClipCursor(&rc);
	Sleep(10000);
	ClipCursor(NULL);
	
	return 0;
}
