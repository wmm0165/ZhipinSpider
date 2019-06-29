# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhipinspiderPipeline(object):
    def process_item(self, item, spider):
        print("工作:" , item['title'])
        print("工资:" , item['salary'])
        print("工作地点:" , item['work_addr'])
        print("详情链接:" , item['url'])

        print("公司:" , item['company'])
        print("行业:" , item['industry'])
        print("公司规模:" , item['company_size'])

        print("招聘人:" , item['recruiter'])
        print("发布日期:" , item['publish_date'])
