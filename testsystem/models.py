from datetime import datetime

from django.db import models
from django.conf import settings

# Create your models here.
IDENTITIES = (
    ('student', '学生'),
    ('teacher', '教师'),
)

SYMBOLS = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
)


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField('姓名', max_length=128)
    idcard = models.CharField('学号', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    sex = models.CharField('性别', max_length=32, choices=gender, default="男")
    birthday = models.DateField('生日', default=datetime.now())
    c_time = models.DateTimeField('注册时间', auto_now_add=True)
    # avatar = models.FileField(upload_to='avatars/', default="{% static 'login/image/student.jpg' %}")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Paper(models.Model):
    paper_text = models.CharField('试卷标题', max_length=30)
    pub_date = models.DateTimeField('发布日期', auto_now_add=True)
    time = models.TimeField("限时")

    def __str__(self):
        return self.paper_text

    class Meta:
        verbose_name = '试卷'
        verbose_name_plural = verbose_name


class SC_question(models.Model):
    SC_text = models.CharField('单选题内容', max_length=200)
    SC_solution = models.CharField('单选题答案', max_length=1, choices=SYMBOLS)
    value = models.DecimalField('分值', max_digits=4, decimal_places=1)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return "sc_question{}".format(self.id)

    class Meta:
        verbose_name = '单选题'
        verbose_name_plural = verbose_name


class MC_question(models.Model):
    MC_text = models.CharField('多选题内容', max_length=200)
    MC_solution = models.CharField('多选题答案', max_length=6)
    value = models.DecimalField('分值', max_digits=4, decimal_places=1)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return "mc_question{}".format(self.id)

    class Meta:
        verbose_name = '多选题'
        verbose_name_plural = verbose_name


class Blank_question(models.Model):
    blank_text = models.CharField('填空题内容', max_length=200)
    blank_solution = models.CharField('填空题答案', max_length=20)
    value = models.DecimalField('分值', max_digits=4, decimal_places=1)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return "blank_question{}".format(self.id)

    class Meta:
        verbose_name = '填空题'
        verbose_name_plural = verbose_name


class SC_choice(models.Model):
    choice_symbol = models.CharField('选项符号', max_length=1, choices=SYMBOLS)
    choice_text = models.CharField('选项内容', max_length=200)
    question = models.ForeignKey(SC_question, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '单选题选项'
        verbose_name_plural = verbose_name


class MC_choice(models.Model):
    choice_symbol = models.CharField('选项符号', max_length=1, choices=SYMBOLS)
    choice_text = models.CharField('选项内容', max_length=200)
    question = models.ForeignKey(MC_question, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '多选题选项'
        verbose_name_plural = verbose_name


class Score(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    score = models.DecimalField('分数', max_digits=4, decimal_places=1)
    answer = models.CharField('答题卡', max_length=3072)
    time = models.TimeField('答题计时')

    def __str__(self):
        return '{}-{}'.format(self.paper_id, self.user_id)

    class Meta:
        verbose_name = '成绩'
        verbose_name_plural = verbose_name
        ordering = ['paper_id', '-score']


class File(models.Model):
    file = models.FileField("上传试卷", upload_to=settings.FILE_ROOT)
    name = models.CharField("试卷名称", max_length=200)
    time = models.TimeField("限时")

    class Meta:
        db_table = 'test_file'
        verbose_name = "文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
