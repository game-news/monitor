package service

import "gamenews.niracler.com/monitor/model"

func GetGames(pageNum int, pageSize int, maps interface{}) (count int, games []model.Game) {
	db := GetDB()
	db.Where(maps).Offset(pageNum).Limit(pageSize).Find(&games)
	db.Model(&model.Game{}).Where(maps).Count(&count)

	return count, games
}

func AddGame(game *model.Game) bool {
	db := GetDB()
	db.Create(game)

	return true
}
