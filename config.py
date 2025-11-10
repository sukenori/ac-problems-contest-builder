# データベースのファイル名
dbname = 'problems.sqlite3'
# コンテストセット一覧
contest_sets = [
    {
        'name': 'Daily_Training',
        'title': 'Daily Training %-y/%-m/%-d',
        'memo': '毎日 茶(650-800)／緑(800-950)／緑(950-1100)',
        'everyday_start_time': '21:00',
        'duration_second': 5400,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (650, 800),
                'point': 350,
                'include_experimental': True,
                'duplicate_remove_days': 0
            },
            {
                'difficulty_range': (800, 950),
                'point': 400,
                'include_experimental': True,
                'duplicate_remove_days': 0
            },
            {
                'difficulty_range': (950, 1100),
                'point': 450,
                'include_experimental': True,
                'duplicate_remove_days': 0
            }
        ]
    }
]
