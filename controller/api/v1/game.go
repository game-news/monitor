package v1

import (
	"log"
	"net/http"

	"gamenews.niracler.com/monitor/model"
	"github.com/gin-gonic/gin"
)

func GetGames(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"results": "pong",
	})
}

func AddGame(c *gin.Context) {
	game := model.Game{}
	err := c.BindJSON(&game)
	if err != nil {
		log.Fatal(err)
	}

	c.JSON(http.StatusCreated, game)
}

func EditGame(c *gin.Context) {
}

func DeleteGame(c *gin.Context) {
}
