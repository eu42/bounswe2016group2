package com.example.bounswegroup2.Models;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.io.Serializable;

/**
 * Created by Enes on 17.12.2016.
 */
public class RestaurantRate implements Serializable{
    @SerializedName("id")
    @Expose
    private Integer id;
    @SerializedName("score")
    @Expose
    private float score;
    @SerializedName("user")
    @Expose
    private Integer user;
    @SerializedName("restaurant")
    @Expose
    private Integer restaurant;

    /**
     * Gets id.
     *
     * @return the id
     */
    public Integer getId() {
        return id;
    }

    /**
     * Sets id.
     *
     * @param id the id
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * Gets score.
     *
     * @return the score
     */
    public float getScore() {
        return score;
    }

    /**
     * Sets score.
     *
     * @param score the score
     */
    public void setScore(float score) {
        this.score = score;
    }

    /**
     * Gets user.
     *
     * @return the user
     */
    public Integer getUser() {
        return user;
    }

    /**
     * Sets user.
     *
     * @param user the user
     */
    public void setUser(Integer user) {
        this.user = user;
    }

    /**
     * Gets restaurant.
     *
     * @return the restaurant
     */
    public Integer getRestaurant() {
        return restaurant;
    }

    /**
     * Sets restaurant.
     *
     * @param restaurant the restaurant
     */
    public void setRestaurant(Integer restaurant) {
        this.restaurant = restaurant;
    }
}
