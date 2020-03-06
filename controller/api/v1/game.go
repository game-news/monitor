package v1

import (
	"log"
	"net/http"

	"gamenews.niracler.com/monitor/model"
	"gamenews.niracler.com/monitor/service"
	"gamenews.niracler.com/monitor/setting"
	"gamenews.niracler.com/monitor/util"
	"github.com/gin-gonic/gin"
)

func GetGames(c *gin.Context) {
	maps := make(map[string]interface{})
	count, games := service.GetGames(util.GetPage(c), setting.PageSize, maps)

	c.JSON(http.StatusOK, gin.H{
		"count":   count,
		"results": games,
	})
}

func AddGame(c *gin.Context) {
	game := &model.Game{}

	err := c.BindJSON(game)
	if err != nil {
		log.Panicln(err)
	}

	service.AddGame(game)

	c.JSON(http.StatusCreated, game)
}

func EditGame(c *gin.Context) {
}

func DeleteGame(c *gin.Context) {
}
