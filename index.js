const express = require("express");
const mongoose = require("mongoose");
const Lead = require("./models/lead.model");

const app = express();
const port = 8000;

app.use(express.json());

// Routes

app.get("/", (req, res) => {
  res.send("Hello from node api!");
});

app.get("/api/leads", async (req, res) => {
  try {
    const leads = await Lead.find({});
    res.status(200).json(leads);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.get("/api/lead/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const lead = await Lead.findById(id);
    res.status(200).json(lead);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.post("/api/leads", async (req, res) => {
  try {
    const lead = await Lead.create(req.body);
    res.status(200).json(lead);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.put("/api/lead/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const lead = await Lead.findByIdAndUpdate(id, req.body);
    if (!lead) {
      return res.status(404).json({ message: "Lead not found" });
    }
    const updatedLead = await Lead.findById(id);
    res.status(200).json(updatedLead);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.delete("/api/lead/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const lead = await Lead.findByIdAndDelete(id);
    if (!lead) {
      return res.status(404).json({ message: "Lead not found" });
    }
    res.status(200).json({ message: "Lead Deleted Successfully" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// added Node-API in between .net/ and ?
mongoose
  .connect(
    "mongodb+srv://m_abid:MsVyNDQ8TMdi660d@turacoventuresdb.8elsw.mongodb.net/Node-API?retryWrites=true&w=majority&appName=TuracoVenturesDB"
  )
  .then(() => {
    console.log("Connected to db");
    app.listen(port, () => console.log(`Server started on port ${port}`));
  })
  .catch((err) => console.log(err));
