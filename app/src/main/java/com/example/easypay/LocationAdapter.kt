package com.example.easypay

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class LocationAdapter(private val locationList: ArrayList<LocationModel>): RecyclerView.Adapter<LocationAdapter.ViewHolder>() {
    class ViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        val locationName = itemView.findViewById<TextView>(R.id.location_name)
        val locationId = itemView.findViewById<TextView>(R.id.location_id)
        val locationPrice = itemView.findViewById<TextView>(R.id.location_price)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(LayoutInflater.from(parent.context).inflate(R.layout.locationcard, parent, false))
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val location = locationList[position]

        holder.locationName.text = location.locationName
        holder.locationId.text = location.locationId
        holder.locationPrice.text = location.locationPrice
    }

    override fun getItemCount(): Int {
        return locationList.size
    }
}