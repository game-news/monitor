package model

import (
	"time"
)

type Game struct {
	Model
	Name        string     `gorm:"size:128;unique;not null" json:"name"`
	ImgPath     string     `gorm:"size:256" json:"img_path"`
	PublishTime *time.Time `json:"publish_time"`
}
