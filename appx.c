/*
	File: appx.c
	Autore: Arves100
	Descrizione: Chiamata manuale alla rimozione delle applicazione AppX senza passare da PowerShell
	Data: 31 Agosto 2020
*/
#include <stdlib.h>
#include <wchar.h>
#include <Windows.h> // ;)

// LPCWSTR = const wchar_t* (Questa è una stringa UCS-2 [NON UTF16 PERCHE WINDOWS è WINDOWS])
// HRESULT = Sarebbe l'errno_t di Windows
// HMODULE = Sarebbe il tipo puntatore ad oggetti di Windows (vari oggetti)

// Definizione della funzione presa dalla DLL
typedef __int64 (__fastcall*AppxCallback)(LPCWSTR packageFullName, HRESULT* errors);

int wmain(int argc, wchar_t** argv) // Entrypoint UCS2
{
  LPCWSTR szAppxName = NULL;  
  HMODULE hAppx = NULL;
  HRESULT hErr = S_OK;
  AppxCallback c_appx = NULL;
  __int64 nRet = 0;

  if (argc < 2)
  {
    printf("%S [appx]\n", argv[0]);
    return 0;
  }

  szAppxName = argv[1];

  // Carica la DLL e ne prende il puntatore
  hAppx = LoadLibraryW(L"AppXDeploymentClient.dll");
  if (!hAppx)
  {
    printf("LOADLIBRARY FAIL\n");
    return -1;
  }

  // Prende la posizione della funzione esportata e la salva
  c_appx = (AppxCallback)GetProcAddress(hAppx, "AppxRemovePackageForAllUsers");

  if (!c_appx)
  {
    FreeLibrary(hAppx);
    printf("GETPROCADDRESS FAIL\n");
    return -2;
  }

  nRet = c_appx(szAppxName, &hErr); // Chiamata al callback (funzione DLL)
  printf("%x %x\n", nRet, hErr);
  FreeLibrary(hAppx); // Chiude la libreria precedentemente aperta
  return 0;
}