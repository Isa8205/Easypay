
import android.R
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

class MyAdapter(dataList: List<MyDataModel>) : RecyclerView.Adapter<MyAdapter.ViewHolder?>() {
    private val dataList: List<MyDataModel> = dataList

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var title: TextView = itemView.findViewById<TextView>(R.id.card_title)
        var description: TextView = itemView.findViewById<TextView>(R.id.card_description)
    }

    fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view: View = LayoutInflater.from(parent.context)
            .inflate(R.layout.card_item, parent, false)
        return ViewHolder(view)
    }

    fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val data: MyDataModel = dataList[position]
        holder.title.setText(data.getTitle())
        holder.description.setText(data.getDescription())
    }

    val itemCount: Int
        get() = dataList.size
}