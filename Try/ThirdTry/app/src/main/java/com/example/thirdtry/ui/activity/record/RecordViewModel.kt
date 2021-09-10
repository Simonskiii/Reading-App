package com.example.thirdtry.ui.activity.record

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.thirdtry.api.RetrofitClient
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.model.Comment
import com.example.thirdtry.model.Record

class RecordViewModel: ViewModel() {
    fun getHistory(token: String): MutableLiveData<BaseDataResult<MutableList<Record>>> =
        RetrofitClient.serviceApi.getHistory("JWT $token")
    fun getFav(token: String): MutableLiveData<BaseDataResult<MutableList<Record>>> =
        RetrofitClient.serviceApi.getFav("JWT $token")
    fun getComment(token: String): MutableLiveData<BaseDataResult<MutableList<Comment>>> =
        RetrofitClient.serviceApi.getComment("JWT $token")
}