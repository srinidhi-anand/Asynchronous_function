import asyncio
import time
import aiofiles
import os
import shutil

async def read_file(file_name):
	async with aiofiles.open(os.path.join('.\\source\\',file_name), mode='r') as f:
		print("%s: %s" % ( file_name, time.ctime(time.time()) ))
		return await f.read()


async def main(fileList):
	tasks = []
	for file_name in fileList:
		task = asyncio.ensure_future(read_file(file_name))
		tasks.append(task)
	await  asyncio.gather(*tasks, return_exceptions=True)
	try:
		shutil.copytree(src='.\\source', dst='.\\copy\\')
		print('Files moved to destination!')
	except:
		print('Files already moved to destination!')
	
	

if __name__ == "__main__": 
	fileList = os.listdir('.\\source')
	#fileList = list(file for file in fileList if os.path.splitext(file)[1][1:]  in ('txt'))
	start_time = time.time()
	asyncio.run(main(fileList))
	duration = time.time() - start_time
	print(f"Reads {len(fileList)} files in {duration} seconds")