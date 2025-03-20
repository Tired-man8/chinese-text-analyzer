package main

import (
	"bytes"
	"encoding/json"
	"io"
	"net/http"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

// Request Structure
type RequestBody struct {
	Text string `json:"text"`
}

// Function to call Flask API
func callFlaskAPI(text string) (map[string]interface{}, error) {
	requestBody, _ := json.Marshal(RequestBody{Text: text})

	resp, err := http.Post("http://127.0.0.1:5000/process", "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var result map[string]interface{}
	json.Unmarshal(body, &result)

	return result, nil
}

func main() {
	router := gin.Default()

	router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"http://127.0.0.1:5000"}, // Allow requests from Flask frontend
		AllowMethods:     []string{"GET", "POST", "OPTIONS"},
		AllowHeaders:     []string{"Content-Type"},
		ExposeHeaders:    []string{"Content-Length"},
		AllowCredentials: true,
		MaxAge:           12 * time.Hour,
	}))

	// API route that calls Flask
	router.POST("/process", func(c *gin.Context) {
		var requestBody RequestBody

		if err := c.ShouldBindJSON(&requestBody); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON"})
			return
		}

		// Call Flask API
		result, err := callFlaskAPI(requestBody.Text)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Flask API request failed"})
			return
		}

		// Return processed data
		c.JSON(http.StatusOK, result)
	})

	router.Run(":8080")

}
