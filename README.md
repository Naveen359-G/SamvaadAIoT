# SamvaadAIoT Platform

**Where Devices Converse with Intelligence**

---

## 🎯 About SamvaadAIoT

SamvaadAIoT is an AI-powered IoT platform that enables intelligent device dialogue and real-world awareness through AI-driven IoT and immersive AR visualization.

> **Built on ThingsBoard**: SamvaadAIoT is a customized distribution of the [ThingsBoard](https://thingsboard.io) open-source IoT platform, enhanced with our proprietary features and branding.

### Mission Statement

We enable intelligent device dialogue and real-world awareness through AI-driven IoT and immersive AR visualization.

---

## ✨ Key Features

- **Device Management**: Provision, monitor, and control IoT devices securely
- **Real-time Dashboards**: Visualize data with customizable widgets and stunning SCADA interfaces
- **AI-Powered Analytics**: Intelligent data processing and insights
- **Powerful Rule Engine**: Create complex data processing workflows visually
- **Multi-Protocol Support**: MQTT, HTTP, CoAP, LWM2M, SNMP
- **Scalable Architecture**: From single devices to millions, edge to cloud
- **Real-time Alarms**: Define thresholds and trigger intelligent notifications
- **Multi-Tenancy**: Secure isolation for different organizations and customers

---

## 🚀 Quick Start

### Prerequisites

- Java 17 or higher
- PostgreSQL 12+ (or Cassandra for hybrid mode)
- Node.js 18+ (for building UI)
- Maven 3.6+

### Installation

```bash
# Clone the repository
git clone [your-repository-url]
cd samvaadaiot

# Build the UI
cd ui-ngx
npm install
npm run build:prod

# Build the application
cd ..
mvn clean install -DskipTests

# Run the application
java -jar application/target/thingsboard-*.jar
```

Access the platform at `http://localhost:8080`

**Default Credentials:**
- System Admin: `sysadmin@thingsboard.org` / `sysadmin`

---

## 📖 Documentation

For complete documentation, please refer to the original ThingsBoard documentation:

- [Getting Started Guide](https://thingsboard.io/docs/getting-started-guides/helloworld/)
- [Device Integration](https://thingsboard.io/docs/getting-started-guides/connectivity/)
- [Dashboard Creation](https://thingsboard.io/docs/user-guide/dashboards/)
- [Rule Engine](https://thingsboard.io/docs/user-guide/rule-engine-2-0/re-getting-started/)
- [APIs](https://thingsboard.io/docs/api/)

---

## 🤝 Attribution & License

### Based on ThingsBoard Open Source Platform

**SamvaadAIoT is built upon the excellent work of the ThingsBoard community.**

Original ThingsBoard Project:
- Website: https://thingsboard.io
- GitHub: https://github.com/thingsboard/thingsboard
- Copyright © 2016-2025 The Thingsboard Authors

### What We've Customized

✅ **Branding & UI**: Custom SamvaadAIoT theme with modern color palette  
✅ **Enhanced Features**: AI integrations and advanced analytics  
✅ **Custom Widgets**: Industry-specific visualization components  
✅ **Extended APIs**: Additional endpoints for custom integrations  
✅ **AR Visualization**: (Coming Soon) Immersive data visualization

### License

This project is based on ThingsBoard and is released under the **Apache License 2.0**.

**Copyright:**
- Original ThingsBoard Platform © 2016-2025 The Thingsboard Authors
- SamvaadAIoT Customizations © 2025 [Your Company Name]

See [LICENSE](./LICENSE) file for the full Apache 2.0 license text.  
See [NOTICE](./NOTICE) file for detailed attribution.

---

## 🆘 Support

### For SamvaadAIoT-Specific Features
- Email: support@samvaadaiot.com
- Documentation: [Your documentation URL]

### For Core ThingsBoard Features
- ThingsBoard Documentation: https://thingsboard.io/docs/
- Community Forum: https://groups.google.com/forum/#!forum/thingsboard
- GitHub Issues: https://github.com/thingsboard/thingsboard/issues

---

## 🙏 Acknowledgments

We are grateful to:
- **The ThingsBoard Authors** for creating and maintaining the excellent open-source IoT platform
- **The open-source community** for contributions and support
- **Apache Software Foundation** for the Apache 2.0 license framework

---

**SamvaadAIoT** - Where Devices Converse with Intelligence 🚀

*Empowering the future of IoT with AI-driven intelligence*
