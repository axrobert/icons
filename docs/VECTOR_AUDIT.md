# Traced SVG visual comparison

This report compares **all 126** traced SVGs (rasterized at 64px with CairoSVG) to their 64px PNG counterparts. The metric is mean absolute RGB pixel difference after composition on `#151b22`; 0 means identical. It is **not** an artistic quality score or a perceptual similarity judgment.

- Vector render failures: **0**
- Mean RGB pixel difference (0–255): **7.1**
- Median difference: **7.0**

## Highest differences

| Slug | Difference |
|:--|--:|
| `react` | 11.3 |
| `jaeger` | 10.8 |
| `ollama` | 10.7 |
| `preact` | 10.5 |
| `webpack` | 10.3 |
| `hugging-face` | 10.3 |
| `clickhouse` | 10.2 |
| `datadog` | 9.9 |
| `playwright` | 9.6 |
| `tensorflow` | 9.5 |
| `jupyter` | 9.4 |
| `csharp` | 9.3 |
| `github-actions` | 9.1 |
| `kotlin` | 9.1 |
| `sql-server` | 8.9 |

**Conclusion:** the automatically traced SVG layer should not be chosen as the default visual asset. Keep PNG as the master, and refine particular vectors individually when necessary.
