class Lesson:
    def __init__(self, name, teacher, cabinet, begin_t, end_t):
        self.dict = {
            'time': {
                'begin': begin_t,
                'end': end_t
            },
            'lesson': {
                'lesson_name': name,
                'teacher': teacher,
                'cabinet': cabinet
            }
        }

    def to_dict(self) -> dict:
        return self.dict.copy()


class LessonsArray:
    def __init__(self):
        self.lessons = list()
        self.index = 1

    def add_lesson(self, lesson: Lesson):
        _lesson = lesson.to_dict()
        _lesson['index'] = str(self.index)
        self.index += 1
        self.lessons.append(_lesson)

    def to_list(self):
        return self.lessons.copy()

    def clear(self):
        self.lessons = list()
        self.index = 1
