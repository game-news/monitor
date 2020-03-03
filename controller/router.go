package controller

import (
	v1 "gamenews.niracler.com/monitor/controller/api/v1"
	"gamenews.niracler.com/monitor/setting"
	"github.com/gin-gonic/gin"
)

func MapRoutes() *gin.Engine {
	ret := gin.New()

	ret.Use(gin.Logger())

	ret.Use(gin.Recovery())

	gin.SetMode(setting.RunMode)

	apiv1 := ret.Group("/api/v1")
	apiv1.GET("/game", v1.GetGames)
	apiv1.POST("/game", v1.AddGame)
	apiv1.PUT("/game/:id", v1.EditGame)
	apiv1.DELETE("/game/:id", v1.DeleteGame)

	return ret
}
