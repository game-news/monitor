package model

import (
	"time"
)

type Game struct {
	Model
	Name              string     `gorm:"size:128;unique;not null" json:"name"`
	ImgPath           string     `gorm:"size:256" json:"img_path"`
	PublishTime       *time.Time `json:"-"`
	PublishTimeString string     `gorm:"-" json:"publish_time"`
}

func (game *Game) BeforeSave() error {
	loc, _ := time.LoadLocation("Local")
	the_time, err := time.ParseInLocation("2006-01-02", game.PublishTimeString, loc)
	if err == nil {
		game.PublishTime = &the_time
	}

	return nil
}
