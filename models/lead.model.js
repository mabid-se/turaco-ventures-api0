const mongoose = require("mongoose");
// const sequence = require("mongoose-sequence")(mongoose);

const LeadSchema = new mongoose.Schema(
  {
    // id: { type: Number, unique: true, index: true },
    serial_number: {
      type: String,
      required: [true, "Serial number is required"],
    },
    contact_number: {
      type: String,
      required: [true, "Contact number is required"],
    },
    name: { type: String, required: false },
    persons: { type: String, required: false },
    follow_up: { type: String, required: [true, "Follow up is required"] },
    status: { type: String, required: [true, "Status is required"] },
    destination: { type: String, required: false },
    dates: { type: String, required: false },
    city: { type: String, required: false },
    details: { type: String, required: [true, "Details is required"] },
  },
  { timestamps: true }
);

// LeadSchema.plugin(sequence, { id: "lead_id", inc_field: "id" });

const Lead = mongoose.model("Lead", LeadSchema);

module.exports = Lead;
