Title: Pelican adjustments
Date: 31-05-2013
Summary: some personal adjustments to pelican
Tags: web dev, html/css, programming, python, pelican
Category: sandbox

Modify file `generators.py` line `599`:

	::python
	def generate_output(self, writer):
        self._copy_paths(self.settings['THEME_STATIC_PATHS'], self.theme,
                         'static', self.output_path, os.curdir)
        # copy all Static files
        for sc in self.staticfiles:
            source_path = os.path.join(self.path, sc.source_path)
            save_as = os.path.join(self.output_path, sc.save_as)
            mkdir_p(os.path.dirname(save_as))
            shutil.copy(source_path, save_as)
            logger.info('copying {} to {}'.format(sc.source_path, sc.save_as))

This copies the `static`  folder from the folder `theme`, into the respective folder `static`

