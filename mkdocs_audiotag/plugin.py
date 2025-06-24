import mkdocs
import re
import xml.etree.ElementTree as ET

class AudioTag(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ('autoplay', mkdocs.config.config_options.Type(bool, default=False)),
        ('controls', mkdocs.config.config_options.Type(bool, default=True)),
        ('loop', mkdocs.config.config_options.Type(bool, default=False)),
        ('muted', mkdocs.config.config_options.Type(bool, default=False)),
        ('preload', mkdocs.config.config_options.Type(str, default='metadata')),
        ('width', mkdocs.config.config_options.Type(str, default='100%'))
    )

    def on_page_markdown(self, markdown, page, config, files):
        #surfers = re.finditer(r'<!--\s*audio\s*-->\s*(.+?)<!--\s+-->', markdown, re.DOTALL)
        audio_elements = re.finditer(r'^(?:!\[audio/.+?]\(.+?\)\n)+', markdown, re.M)
        
        for match in audio_elements:
            old_tag = match.group(0)
            sources = re.findall(r'!\[(.+)\]\((.+)\)', old_tag)            

            tag = ET.Element('audio', attrib={'preload': self.config['preload']})

            tag.set('style',f'width:{self.config['width']}')

            # Boolean attributes
            for attribute in ['autoplay', 'controls', 'loop', 'muted']:
                if self.config[attribute]:
                    tag.set(attribute, '')

            for mimetype, file in sources:
                element_class = mimetype.replace('audio/', '')
                ET.SubElement(tag, 'source', attrib={'src': '../' + file, 'type': mimetype, 'class': element_class})
            
            new_tag = ET.tostring(tag, encoding='unicode', method='html') + '\n'
            
            markdown = markdown.replace(old_tag, new_tag, 1)
        
        return markdown
