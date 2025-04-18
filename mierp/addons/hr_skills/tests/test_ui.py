# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp.tests

@mierp.tests.tagged('-at_install', 'post_install')
class SkillsTestUI(mierp.tests.HttpCase):
    def test_ui(self):
        levels = self.env['hr.skill.level'].create([{
            'name': f'Level {x}',
            'level_progress': x * 10,
        } for x in range(10)])
        skill_type = self.env['hr.skill.type'].create({
            'name': 'Best Music',
            'skill_level_ids': levels.ids,
        })
        self.env['hr.skill'].create([{
            'name': 'Fortunate Son',
            'skill_type_id': skill_type.id,
        }, {
            'name': 'Oh Mary',
            'skill_type_id': skill_type.id,
        }])

        self.start_tour("/mierp", 'hr_skills_tour', login='admin')
