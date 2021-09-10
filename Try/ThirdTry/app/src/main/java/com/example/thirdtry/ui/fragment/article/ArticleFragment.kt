package com.example.thirdtry.ui.fragment.article

import androidx.lifecycle.ViewModelProviders
import com.example.thirdtry.R
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.article_fragment.*
import androidx.lifecycle.Observer
import android.os.Handler
import android.view.View
import android.widget.Toast
import com.example.thirdtry.databinding.ArticleItemsLayoutBinding
import com.example.thirdtry.base.BaseFragment
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.model.Article
import com.example.thirdtry.ui.fragment.scheme.SchemeFragment
import com.example.thirdtry.ui.fragment.scheme.SchemeViewPagerAdapter
import kotlinx.android.synthetic.main.article_fragment.sub_view_pager
import kotlinx.android.synthetic.main.article_fragment.tab_layout
import kotlinx.android.synthetic.main.article_subfragment.*
import kotlinx.android.synthetic.main.scheme_fragment_new.*
import kotlin.math.log


class ArticleFragment : BaseFragment() {
    private lateinit var viewModel: ArticleViewModel
    private var articles = mutableListOf<Article>()
    private val adapter: ArticleBindingAdapter by lazy {
        ArticleBindingAdapter(articles)
    }
    private val mObserver: Observer<BaseDataResult<MutableList<Article>>> by lazy {
        Observer<BaseDataResult<MutableList<Article>>> {
            if (it == null){
                Toast.makeText(activity, "无网络连接", Toast.LENGTH_SHORT).show()
                return@Observer
            }
            else{
                if (articles.isEmpty()) {
                    if(!it.subjects.isNullOrEmpty()){
                        this.articles.addAll(it.subjects)
                        adapter.notifyDataSetChanged()
                        spin_kit.visibility = View.GONE
                    }
                    else{
                        spin_kit.visibility = View.GONE
                    }
                }
                else{
                    this.articles.clear()
                    this.articles.addAll(it.subjects)
                    adapter.notifyDataSetChanged()
                }
            }
        }
    }

    override fun getLayoutId(): Int = R.layout.article_fragment

    override fun initViewModel() {
        viewModel = ViewModelProviders.of(this.activity!!).get(ArticleViewModel::class.java)
        viewModel.getArticles(token).observe(this, mObserver)
    }

    override fun initView() {
        tab_layout.setupWithViewPager(sub_view_pager)
        val adapter = ArticleViewPagerAdapter(context!!, this.childFragmentManager)
        sub_view_pager.offscreenPageLimit = 5
        sub_view_pager.adapter = adapter
    }

}


//    private fun initRecyclerView() {
//        //获取RecyclerView
//        var mRecyclerView = view?.findViewById<RecyclerView>(R.id.line_recy_view)
//        //创建adapter
//        mRecyclerAdapter = articleItemsAdapter(this, )
//        //给RecyclerView设置adapter
//        mRecyclerView.setAdapter(mRecyclerAdapter)
//        //设置layoutManager,可以设置显示效果，是线性布局、grid布局，还是瀑布流布局
//        //参数是：上下文、列表方向（横向还是纵向）、是否倒叙
//        mRecyclerView.setLayoutManager(
//            LinearLayoutManager(
//                activity,
//                LinearLayoutManager.VERTICAL,
//                false
//            )
//        )
//        //设置item的分割线
//        mRecyclerView.addItemDecoration(
//            DividerItemDecoration(
//                activity!!,
//                DividerItemDecoration.VERTICAL
//            )
//        )
//        //RecyclerView中没有item的监听事件，需要自己在适配器中写一个监听事件的接口。参数根据自定义
//        mRecyclerAdapter.setOnItemClickListener(object :
//            CollectRecycleAdapter.OnItemClickListener() {
//            fun OnItemClick(view: View, data: GoodsEntity) {
//                //此处进行监听事件的业务处理
//                Toast.makeText(activity, "我是item", Toast.LENGTH_SHORT).show()
//            }
//        })
//    }

