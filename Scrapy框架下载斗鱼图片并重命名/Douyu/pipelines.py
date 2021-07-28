import scrapy
import os
from Douyu.settings import IMAGES_STORE as images_store  # 使用settings文件里的参数
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['image_link']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]

        # 给图片重命名
        os.rename(images_store + image_path[0], images_store + item['nickname'] + '.jpg')
        return item
