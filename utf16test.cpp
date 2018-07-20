#include <stdio.h>
#include <wchar.h>
#include <tchar.h>
#include <locale.h>
#include <limits.h>
#include <stdarg.h>
#include <locale>
#include <io.h>
#include <fstream>
#include <codecvt>
#include <fcntl.h>

std::wofstream fp;
void myprintf(const wchar_t* fmt, ...);

const wchar_t* utfle = L"\xFF\xFE"; //utf16 little-endian
//const wchar_t* utfle = L"\xEF\xBB\xBF";  //utf8 with bom

int _tmain(int argc, TCHAR** argv)
{
#if 0
	const std::locale utf_locale = std::locale(std::locale(), new std::codecvt_utf16<wchar_t>());
	int i = 0;

	_setmode(_fileno(stdout),_O_U16TEXT);
	setlocale(LC_ALL, "");

	fp.open(L"macro_info.txt");
	if (!fp.is_open())
	{
		wprintf(L"Failed to open macro_info.txt");
		return 0;
	}

	fp<<utfle;
	fp.imbue(utf_locale);
	
	myprintf(L"sizeof(char) = %ld\n", sizeof(char));
	myprintf(L"sizeof(wchar_t) = %ld\n", sizeof(wchar_t));
	myprintf(L"sizeof(unsigned char) = %ld\n", sizeof(unsigned char));
	myprintf(L"sizeof(int) = %ld\n", sizeof(int));
	myprintf(L"sizeof(short) = %ld\n", sizeof(short));
	myprintf(L"sizeof(long) = %ld\n", sizeof(long));
	myprintf(L"CHAR_MAX = %d\nCHAR_MIN = %d\nUCHAR_MAX = %d\nSHRT_MAX = %d\nSHRT_MIN = %d\n", CHAR_MAX, CHAR_MIN, UCHAR_MAX, SHRT_MAX, SHRT_MIN);
	fp.close();

#if 0
	fp.open(L"char_table.txt");
	if (!fp.is_open())
	{
		wprintf(L"Failed to open char_table.txt");
		return 0;
	}

	fp<<utfle;
	fp.imbue(utf_locale);	
	
	myprintf(L"Dump table: char\n");
	
	for (i = CHAR_MIN; i < CHAR_MAX; i++)
		myprintf(L"%d: %c\n", i, (char)i);
	
	fp.close();

	fp.open(L"wchar_table.txt");
	if (!fp.is_open())
	{
		wprintf(L"Failed to open wchar_table.txt");
		return 0;
	}
	
	fp<<utfle;
	fp.imbue(utf_locale);	
	
	myprintf(L"Dump table: wchar_t\n");
	
	for(i = SHRT_MIN; i < SHRT_MAX; i++)
		myprintf(L"%d: %C\n", i, (wchar_t)i);
	
	fp.close();
#endif
#endif
	wprintf(L"%d?%d", (int)L'A', (int)'A');
	wprintf(L"DONE!");
	return 0;
}

void myprintf(const wchar_t* fmt, ...)
{
	va_list vl;
	va_start(vl, fmt);
	
	int n = _vscwprintf(fmt, vl);
	
	wchar_t* t = (wchar_t*)malloc(sizeof(wchar_t)*(1+n));
	
	vswprintf(t, fmt, vl);
	
	wprintf(t);
	
	va_end(vl);
	
	fp<<t;
	
	free(t);
}
