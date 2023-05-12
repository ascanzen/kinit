# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2021/12/5 8:45
# @File           : file_manage.py
# @IDE            : PyCharm
# @desc           : 保存图片到本地

import datetime
import os
import shutil
from application.settings import TEMP_DIR, STATIC_ROOT, BASE_DIR, STATIC_URL, STATIC_DIR
from fastapi import UploadFile
import sys
from utils.file.file_base import FileBase
from aiopathlib import AsyncPath as Path
import aioshutil


class FileManage(FileBase):
    """
    上传文件管理
    """

    def __init__(self, file: UploadFile, path: str):
        self.path = self.generate_path(path, file.filename)
        self.file = file

    async def save_image_local(self, accept: list = None) -> dict:
        """
        保存图片文件到本地
        """
        if accept is None:
            accept = self.IMAGE_ACCEPT
        await self.validate_file(self.file, max_size=5, mime_types=accept)
        return await self.save_local()

    async def save_local(self) -> dict:
        """
        保存文件到本地
        """
        path = self.path
        if sys.platform == "win32":
            path = self.path.replace("/", "\\")
        # save_path = os.path.join(STATIC_ROOT, path)
        save_path = Path(STATIC_ROOT) / path
        if not await save_path.parent.exists():
            await save_path.parent.mkdir(parents=True, exist_ok=True)
        await save_path.write_bytes(await self.file.read())
        return {
            "local_path": f"{STATIC_DIR}/{self.path}",
            "remote_path": f"{STATIC_URL}/{self.path}"
        }

    @staticmethod
    async def save_tmp_file(file: UploadFile):
        """
        保存临时文件
        """
        date = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
        # file_dir = os.path.join(TEMP_DIR, date)
        file_dir = Path(TEMP_DIR) / date
        if not await file_dir.exists():
            await file_dir.mkdir(parents=True, exist_ok=True)
        filename = file_dir / str(int(datetime.datetime.now().timestamp())) + file.filename
        await filename.write_bytes(await self.file.read())
        return str(filename)

    @staticmethod
    def copy(src: str, dst: str):
        """
        复制文件
        根目录为项目根目录，传过来的文件路径均为相对路径

        :param src: 原始文件
        :param dst: 目标路径。绝对路径
        """
        if src[0] == "/":
            src = src.lstrip("/")
        if sys.platform == "win32":
            src = src.replace("/", "\\")
            dst = dst.replace("/", "\\")
        src = os.path.join(BASE_DIR, src)
        if not os.path.exists(os.path.dirname(dst)):
            os.mkdir(os.path.dirname(dst))
        shutil.copyfile(src, dst)

    async def async_copy(src: str, dst: str):
        if src[0] == "/":
            src = src.lstrip("/")
        if sys.platform == "win32":
            src = src.replace("/", "\\")
            dst = dst.replace("/", "\\")
        src = Path(BASE_DIR) / src
        dst = Path(dst)
        if not await dst.parent.exists():
            await dst.parent.mkdir(parents=True, exist_ok=True)
        await aioshutil.copyfile(src, dst)

if __name__ == '__main__':
    # src = r"D:\ktianc\private\vv-reserve\reserve-api\static\system\2022-12-07\16703958210ab33912.ico"
    # dst = r"D:\ktianc\private\vv-reserve\reserve-api\static\system\favicon.ico"
    # shutil.copyfile(src, dst)
    pass
