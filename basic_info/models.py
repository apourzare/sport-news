from django.db import models

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=30, verbose_name='عنوان سایت')
    instagram_page = models.URLField(null=True, blank=True,verbose_name='صفحه اینستاگرام')
    youtube_channel = models.URLField(null=True, blank=True,verbose_name='کانال یوتیوب')
    status = models.BooleanField(default=False, verbose_name='وضعیت سایت')
    
    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیم ها'

    def __str__(self):
        return self.site_title
