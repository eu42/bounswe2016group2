package com.example.bounswegroup2.Utils;

import com.example.bounswegroup2.Models.Diet;
import com.example.bounswegroup2.Models.Food;
import com.example.bounswegroup2.Models.FoodLess;
import com.example.bounswegroup2.Models.Ingredient;
import com.example.bounswegroup2.Models.Restaurant;
import com.example.bounswegroup2.Models.User;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.json.JSONObject;

import java.util.List;
import java.util.Map;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.DELETE;
import retrofit2.http.Field;
import retrofit2.http.FieldMap;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.Headers;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;
import retrofit2.http.Query;
import retrofit2.http.QueryMap;

/**
 * This interface is to define endpoints
 * Created by Enes on 29.10.2016.
 */

public interface ApiInterface {

    String BASE_URL="http://52.213.193.130/";
    Retrofit retrofit = new Retrofit.Builder()
            .baseUrl(ApiInterface.BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build();

    @FormUrlEncoded
    @Headers("Content-Type: application/json")
    @PUT("api/users/signup/{userInfo}")
    Call<ResponseBody> postSignupUser(@FieldMap(encoded = true) Map<String,String> userInfo);

    @FormUrlEncoded
    @Headers("Content-Type: application/json")
    @POST("api/users/signin/{userInfo}")
    Call<ResponseBody> postSigninUser(@FieldMap(encoded = true) Map<String, String> userInfo);

    @POST("api/users/signout")
    void postSignout();

    @GET("api/users/signout")
    void getSignout();

    @POST("api/users/me")
    void sendYourself();

    @GET("api/users/me")
    void getYourself();

    @GET("api/users")
    Call<List<User>> getUsers(@QueryMap Map<String, String> options);

    @GET("api/users/{userId}")
    void getUserWithId();

    @PUT("api/users/{userId}")
    void putUserWithId();

    @DELETE("api/users/{userId}")
    void deleteUserWithId();

    @Headers("Content-Type: application/json")
    @GET("api/ingredients")
    Call<List<Ingredient>> getIngredients(@QueryMap Map<String, String> options);

    @POST("api/ingredients")
    void sendIngredients();

    @Headers("Content-Type: application/json")
    @GET("api/foods")
    Call<List<FoodLess>> getFoods();



    @Headers("Content-Type: application/json")
    @POST("/api/foods/{foodId}/ate")
    Call<Response> eatFood(@Path("foodId") int foodId);

    @Headers("Content-Type: application/json")
    @POST("/api/foods/{foodId}/comment")
    Call<Response> commentFood(@Path("foodId") int foodId);

    @Headers("Content-Type: application/json")
    @POST("/api/foods/{foodId}/rate")
    Call<Food> rateFood(@Path("foodId") int foodId);

    @Headers("Content-Type: application/json")
    @GET("api/foods/{foodId}")
    Call<Food> getFoodWithId(@Path("foodId") int foodId);
     @Headers("Content-Type: application/json")
     @POST("api/searchFood")
     Call<List<Food>> searchFood(@Query("query") String query);


    @Headers("Content-Type: application/json")
    @GET("api/diets")
    Call<List<Diet>> getDiets();

    @Headers("Content-Type: application/json")
    @GET("api/myDiets")
    Call<List<Diet>> getMyDiets();

    @Headers("Content-Type: application/json")
    @POST("api/myDiets/{dietId}")
    Call<List<Diet>> setMyDiet(@Path("dietId") int dietId);

    @Headers("Content-Type: application/json")
    @GET("api/restaurants")
    Call<List<Restaurant>> getRestaurants();

    @Headers("Content-Type: application/json")
    @GET("api/restaurants/{restaurantId}")
    Call<Restaurant> getRestaurantWithId(@Path("restaurantId") int restaurantId);

    @Headers("Content-Type: application/json")
    @POST("api/restaurants/{restaurantId}/comment")
    Call<Response> commentRestaurant(@Path("restaurantId") int restaurantId);

    @Headers("Content-Type: application/json")
    @POST("api/restaurants/{restaurantId}/rate")
    Call<Response> rateRestaurant(@Path("restaurantId") int restaurantId);

}