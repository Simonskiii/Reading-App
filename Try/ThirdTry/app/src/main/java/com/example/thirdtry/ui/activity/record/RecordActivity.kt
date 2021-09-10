package com.example.thirdtry.ui.activity.record

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.thirdtry.R
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.databinding.ActivityArticleDetialBinding
import com.example.thirdtry.model.Article
import com.example.thirdtry.model.Comment
import com.example.thirdtry.model.Record
import com.example.thirdtry.ui.activity.articleDetail.ArticleDetialActivity
import com.example.thirdtry.ui.activity.articleDetail.ArticleDetialViewModel
import kotlinx.android.synthetic.main.activity_article_detial.*
import kotlinx.android.synthetic.main.activity_record.*
import kotlinx.android.synthetic.main.activity_record.spin_kit
import org.greenrobot.eventbus.EventBus
import org.greenrobot.eventbus.Subscribe
import org.greenrobot.eventbus.ThreadMode

class RecordActivity : AppCompatActivity() {
    companion object {
        lateinit var instance: RecordActivity
    }

    private var records = mutableListOf<Record>()
    private var comments = mutableListOf<Comment>()
    private var type: String? = null
    private lateinit var viewModel: RecordViewModel
    private lateinit var token: String
    private val recordAdapter: RecordBindingAdapter by lazy {
        RecordBindingAdapter(records)
    }
    private val commentAdapter: CommentBindingAdapter by lazy {
        CommentBindingAdapter(comments)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_record)
        EventBus.getDefault().register(this)
        record_rv.layoutManager = LinearLayoutManager(this)
    }

    private val mObserver: Observer<BaseDataResult<MutableList<Record>>> by lazy {
        Observer<BaseDataResult<MutableList<Record>>> {
            if (it == null) {
                Toast.makeText(this, "网络开小差了，请稍后", Toast.LENGTH_SHORT).show()
                return@Observer
            } else {
                if (records.isEmpty() && !it.subjects.isNullOrEmpty()) {
                    this.records.addAll(it.subjects)
                    recordAdapter.notifyDataSetChanged()
                    spin_kit.visibility = View.GONE
                }
            }
        }
    }
    private val mObserver1: Observer<BaseDataResult<MutableList<Comment>>> by lazy {
        Observer<BaseDataResult<MutableList<Comment>>> {
            if (it == null) {
                Toast.makeText(this, "网络开小差了，请稍后", Toast.LENGTH_SHORT).show()
                return@Observer
            } else {
                if (comments.isEmpty()) {
                    if(!it.subjects.isNullOrEmpty()) {
                        this.comments.addAll(it.subjects)
                        commentAdapter.notifyDataSetChanged()
                        spin_kit.visibility = View.GONE
                    }
                    else{
                        spin_kit.visibility = View.GONE
                    }
                }
            }
        }
    }

    @Subscribe(threadMode = ThreadMode.MAIN, sticky = true)
    fun onMessageEvent(event: String) {
        this.type = event
        viewModel = ViewModelProviders.of(this).get(RecordViewModel::class.java)
        val s = getSharedPreferences("loginToken", Context.MODE_PRIVATE)
        token = s.getString("token", "")!!
        when (type) {
            "fav" -> {
                viewModel.getFav(token).observe(this, mObserver)
                record_type.text = "我的收藏"
                record_rv.adapter = recordAdapter
            }
            "history" -> {
                viewModel.getHistory(token).observe(this, mObserver)
                record_type.text = "阅读历史"
                record_rv.adapter = recordAdapter
            }
            "comment" -> {
                viewModel.getComment(token).observe(this, mObserver1)
                record_type.text = "我的评论"
                record_rv.adapter = commentAdapter
            }
        }

    }
}
