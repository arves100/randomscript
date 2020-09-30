#define _CRT_SECURE_NO_WARNINGS
#include <SDL2/SDL.h>
#include <cstdio>
#include <cstring>
#include <cstdint>
#include <vector>
#include <ctime>

struct Image
{
	uint32_t w, h;
	SDL_Surface* pSurface;
};

#undef main

int main(int argc, char* argv[])
{
	printf("dctest\n");

	if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
	{
		printf("%s\n", SDL_GetError());
		return 0;
	}

	SDL_Window* pWindow = SDL_CreateWindow(u8"£ä£ã£ô£å£ó£ô", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, SDL_WINDOW_ALLOW_HIGHDPI | SDL_WINDOW_RESIZABLE);

	SDL_Event e;
	bool quit = false;

	time_t t = time(nullptr);
	printf("PERFORMANCE_START %s\n", asctime(gmtime(&t)));

	FILE* fp = nullptr;
	fopen_s(&fp, argv[1], "rb");

	char header[12];
	memset(header, 0, sizeof(header));
	fread(header, 11, 1, fp);

	if (strcmp(header, "DCSPRITE10") != 0)
	{
		printf("Header %s not supported\n", header);
		return 0;
	}

	uint32_t images;
	fread(&images, sizeof(images), 1, fp);
	std::vector<Image> imgs;
	uint32_t i = 0;
	for (; i < images; i++)
	{
		Image img;
		fread(&img.w, sizeof(img.w), 1, fp);
		imgs.push_back(img);
	}
	for (i = 0; i < images; i++)
	{
		Image& img = imgs[i];
		fread(&img.h, sizeof(img.h), 1, fp);
	}

	uint32_t allsize;
	fread(&allsize, sizeof(allsize), 1, fp);

	std::vector<uint32_t> offsets;
	offsets.resize(images);
	offsets.reserve(images);
	fread(offsets.data(), sizeof(uint32_t), images, fp);
	std::vector<uint16_t> imgdata;
	imgdata.resize(allsize);
	imgdata.reserve(allsize);
	fread(imgdata.data(), sizeof(uint16_t), allsize, fp);

	fclose(fp);


	for (uint32_t fc = 0; fc < images; fc++)
	{
		uint64_t off = offsets[fc];
		uint16_t h = *imgdata.data(); // y
		off++;

		Image& img = imgs[fc];
		img.pSurface = SDL_CreateRGBSurfaceWithFormat(0, img.w, img.h, 16, SDL_PIXELFORMAT_RGBA8888);
		SDL_LockSurface(img.pSurface);

		uint8_t* pixels = (uint8_t*) img.pSurface->pixels;

		for (i = 0; i < h; i++)
		{
			uint16_t runCount = *(imgdata.data() + off);
			off++;

			uint16_t runOffset = 0, runLength = 0;
			uint32_t x = 0;
			for (; runCount > 0; runCount--)
			{
				runOffset += *(imgdata.data() + off);
				runLength = *(imgdata.data() + off + 1);
				x += runOffset;
				off += 2;
				if (runLength > 0)
				{
					uint16_t color = *(imgdata.data() + off);

					for (uint32_t k = 0; k < runLength; k++)
					{
						#define DRPG_RED(p)			( ( ( p ) >> 11 ) & 0x1f )
#define DRPG_GREEN(p)		( ( ( p ) >> 5 ) & 0x3f )
#define DRPG_BLUE(p)		( ( p ) & 0x1f )

						pixels[x] = DRPG_RED(color) << 3;
						pixels[x + 1] = DRPG_GREEN(color) << 3;
						pixels[x + 2] = DRPG_BLUE(color) << 3;
						pixels[x + 3] = 255;
						x += 4;
					}
				}

				runOffset += runLength;
				off += runLength;
			}
		}

		SDL_UnlockSurface(img.pSurface);
	}

	time_t t2 = time(nullptr);
	printf("PERFORMANCE_END %s\n", asctime(gmtime(&t)));
	time_t tx = t2 - t;
	printf("ELAPSED TIME: %llu\n", tx);

	SDL_Surface* pWinSurface = SDL_GetWindowSurface(pWindow);

	SDL_FillRect(pWinSurface, NULL, SDL_MapRGB(pWinSurface->format, 255, 255, 255));

	SDL_Rect ds;
	ds.x = 200;
	ds.y = 200;
	ds.w = imgs[0].w;
	ds.h = imgs[0].h;
	//Apply the image
	SDL_BlitSurface(imgs[0].pSurface, NULL, pWinSurface, &ds);

	SDL_UpdateWindowSurface(pWindow);

	while (!quit)
	{
        // Handle events on queue
        while( SDL_PollEvent(&e) != 0 )
        {
            // User requests quit
            if(e.type == SDL_QUIT)
            {
                quit = true;
            }
        }

	}

	SDL_DestroyWindow(pWindow);

	SDL_Quit();
	return 0;
}
